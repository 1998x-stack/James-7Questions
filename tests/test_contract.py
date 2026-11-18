import json
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
import build
class ContractTests(unittest.TestCase):
    def test_case_schema(self):
        cases=build.load_cases()
        self.assertGreaterEqual(len(cases),1)
        for case in cases:
            self.assertTrue(build.validate(case))
            self.assertEqual(len(case['frameworks']['james']['steps']),7)
            self.assertEqual(len(case['frameworks']['porter']['steps']),5)
            self.assertEqual(len(case['frameworks']['dmaic']['steps']),5)
    def test_reports_exist(self):
        for case in build.load_cases():
            slug=case['id']
            for method in build.METHODS:
                for ext in ('html','md','pdf'):
                    p=ROOT/'docs'/'cases'/slug/(f'{method}.{ext}' if ext=='html' else f'downloads/{method}.{ext}')
                    self.assertTrue(p.is_file(),str(p))
                    self.assertGreater(p.stat().st_size,750,str(p))
    def test_pdfs_have_chinese_text(self):
        try:import fitz
        except ImportError:return
        for case in build.load_cases():
            for method in build.METHODS:
                p=ROOT/'docs'/'cases'/case['id']/'downloads'/f'{method}.pdf'
                doc=fitz.open(p)
                self.assertGreaterEqual(doc.page_count,2,p.name)
                self.assertIn(case['company'].split()[0], ''.join(page.get_text() for page in doc),p.name)
    def test_html_interactive_and_disclaimer(self):
        for case in build.load_cases():
            for method in build.METHODS:
                html=(ROOT/'docs'/'cases'/case['id']/f'{method}.html').read_text('utf-8')
                self.assertIn('window.CASE_DATA',html)
                self.assertIn('id="app"',html)
                self.assertIn(case['caveat'],html)
                self.assertIn('data-idx',html)
    def test_multi_case_isolation(self):
        cases=build.load_cases()
        if len(cases) < 2:return
        self.assertEqual(len({case['id'] for case in cases}),len(cases))
        for case in cases:
            for method in build.METHODS:
                folder=ROOT/'docs'/'cases'/case['id']
                md=(folder/'downloads'/f'{method}.md').read_text('utf-8')
                self.assertIn(case['title'],md)
                self.assertIn(case['caveat'],md)
                for other in cases:
                    if case['id']!=other['id']:
                        self.assertNotIn(other['title'],md)
        index=(ROOT/'docs'/'index.html').read_text('utf-8')
        for case in cases:self.assertIn(case['title'],index)

    def test_new_case_is_unpublished_draft(self):
        from tempfile import TemporaryDirectory
        sys.path.insert(0, str(ROOT))
        from tools.new_case import create_draft
        with TemporaryDirectory() as temp:
            draft=create_draft('sample-business-2027','Sample Co','Future Growth','Software','2027',temp)
            raw=json.loads(draft.read_text('utf-8'))
            self.assertEqual(draft.name,'draft.case.json')
            self.assertEqual(raw['status'],'草稿，禁止发布')
            self.assertFalse(raw['sources'])
            self.assertEqual(len(raw['frameworks']['james']['steps']),7)

    def test_platform_adapters(self):
        for engine in ('.agent','.pi','.claude'):
            for name in ('market-structure','socratic-audit','james-seven-questions','dmaic-execution','evidence-verification','case-publishing'):
                self.assertTrue((ROOT/engine/'skills'/name/'SKILL.md').exists())
                for d in ('references','scripts','assets'):
                    self.assertTrue((ROOT/engine/'skills'/name/d).exists())
if __name__=='__main__':unittest.main()
