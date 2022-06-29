import unittest,os,time,HTMLTestRunner
current_path = os.path.dirname(__file__)
report_path = os.path.join(current_path,'report')
cases_path = os.path.join(current_path,'test_cases')
html_path = os.path.join(report_path,'report_%s.html'%time.strftime('%Y_%m_%d_%H_%M_%S'))

discover = unittest.defaultTestLoader.discover(start_dir=cases_path,
                                               pattern='*_case.py',
                                               top_level_dir=cases_path)
main_suite = unittest.TestSuite()
main_suite.addTest(discover)
file = open(html_path,'wb')
html_runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='禅道UI自动化测试项目', description='由自动化测试组完成，包含大部分功能的自动化测试')
html_runner.run(main_suite)
