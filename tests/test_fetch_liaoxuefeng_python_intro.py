import importlib.util
import unittest
from pathlib import Path


def load_module():
    module_path = Path("scripts/fetch_liaoxuefeng_python_intro.py")
    spec = importlib.util.spec_from_file_location(
        "fetch_liaoxuefeng_python_intro", module_path
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


SAMPLE_INDEX_HTML = """
<a href="/books/python/history/index.html">历史</a>
<a href="/books/python/basic/index.html">Python基础</a>
<a href="/books/python/basic/data-types/index.html">数据类型和变量</a>
<a href="/books/python/function/index.html">函数</a>
<a href="/books/python/function/call-function/index.html">调用函数</a>
<a href="/books/python/basic/data-types/index.html">重复</a>
"""


class FetchLiaoxuefengPythonIntroTest(unittest.TestCase):
    def test_extract_chapter_urls_starts_from_basic_and_keeps_unique_order(self):
        module = load_module()

        urls = module.extract_chapter_urls(SAMPLE_INDEX_HTML)

        self.assertEqual(
            urls,
            [
                "/books/python/basic/index.html",
                "/books/python/basic/data-types/index.html",
                "/books/python/function/index.html",
                "/books/python/function/call-function/index.html",
            ],
        )

    def test_build_page_file_name_is_stable(self):
        module = load_module()

        name = module.build_page_file_name(
            order=7,
            chapter_url="/books/python/function/call-function/index.html",
        )

        self.assertEqual(name, "007-books-python-function-call-function-index-html.json")


if __name__ == "__main__":
    unittest.main()
