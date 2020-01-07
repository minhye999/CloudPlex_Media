# Welcome
from staging.Chrome.CORE.Welcome import * # from 경로+파일 import 사용할 class나 함수
# Pipeline Select
from staging.Chrome.CORE.ProjectSelect import *
# Common
from staging.Chrome.CORE.Gnb import *
from staging.Chrome.CORE.Lnb import *
from staging.Chrome.CORE.Fnb import *
# Create Job
from staging.Chrome.CORE.CreateJob import *
from staging.Chrome.CORE.PopUp_PipelineDetail import *
from staging.Chrome.CORE.PopUp_ProfileDetail import *
from staging.Chrome.CORE.PopUp_Local_SelectFiles import *
from staging.Chrome.CORE.PopUp_S3_SelectFiles import *
from staging.Chrome.CORE.PopUp_SelectCategories import *
# Videos
from staging.Chrome.CORE.Videos import *
from staging.Chrome.CORE.Videos_Detail import *
from staging.Chrome.CORE.Videos_QuickView import *
from staging.Chrome.CORE.PopUp_Publish import *
from staging.Chrome.CORE.PopUp_ProfileDetail import *
# Assets
from staging.Chrome.CORE.Assets import *
from staging.Chrome.CORE.Assets_Create import *
from staging.Chrome.CORE.Assets_Create_Caption import *
from staging.Chrome.CORE.Assets_Create_Image import *
from staging.Chrome.CORE.Assets_Create_Mp3 import *
from staging.Chrome.CORE.Assets_Create_Mp4 import *
from staging.Chrome.CORE.Assets_QuickView import *
# Streams
# Listings
# Channels

import unittest

#from 파일명(라이브러리) import 함수이름 : 파일에서 함수를 가져온다 (전체함수 :* 사용)

if __name__ == "__main__":
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Welcome) #test할 class명
    suite2 = unittest.TestLoader().loadTestsFromTestCase(ProjectSelect)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(Gnb)
    suite4 = unittest.TestLoader().loadTestsFromTestCase(Lnb)
    suite5 = unittest.TestLoader().loadTestsFromTestCase(Fnb)
    suite6 = unittest.TestLoader().loadTestsFromTestCase(CreateJob)
    suite7 = unittest.TestLoader().loadTestsFromTestCase(PopUp_PipelineDetail)
    suite8 = unittest.TestLoader().loadTestsFromTestCase(PopUp_ProfileDetail)
    suite9 = unittest.TestLoader().loadTestsFromTestCase(PopUp_Local_SelectFiles)
    suite10 = unittest.TestLoader().loadTestsFromTestCase(PopUp_S3_SelectFiles)
    suite11 = unittest.TestLoader().loadTestsFromTestCase(PopUp_SelectCategories)
    suite12 = unittest.TestLoader().loadTestsFromTestCase(Videos)
    suite13 = unittest.TestLoader().loadTestsFromTestCase(Videos_Detail)
    suite14 = unittest.TestLoader().loadTestsFromTestCase(Videos_QuickView)
    suite15 = unittest.TestLoader().loadTestsFromTestCase(PopUp_Publish)
    suite16 = unittest.TestLoader().loadTestsFromTestCase(Assets)
    suite17 = unittest.TestLoader().loadTestsFromTestCase(Assets_Create)
    suite18 = unittest.TestLoader().loadTestsFromTestCase(Assets_Create_Caption)
    suite19 = unittest.TestLoader().loadTestsFromTestCase(Assets_Create_Image)
    suite20 = unittest.TestLoader().loadTestsFromTestCase(Assets_Create_Mp3)
    suite21 = unittest.TestLoader().loadTestsFromTestCase(Assets_Create_Mp4)
    suite22 = unittest.TestLoader().loadTestsFromTestCase(Assets_QuickView)

    suite = unittest.TestSuite([suite1, suite2, suite3, suite4, suite5, suite6, suite7, suite8, suite9, suite10,
                                suite11, suite12, suite13, suite14, suite15, suite16, suite17, suite18, suite19, suite20,
                                suite21, suite22])
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        combine_reports = True ,
        add_timestamp = True ,
        report_name = "Test Results(Test Suite)",
        output="../../../staging/Chrome/Test_Results/Reports"
        )).run(suite)

    #TestLoader Class : unittest package에서 Test Suite를 만드는데 사용되는 Class
    #loadTestsFromTestCase : TestLoader Class의 메소드 (Test Case의 Class에서 Testcase를 반환)