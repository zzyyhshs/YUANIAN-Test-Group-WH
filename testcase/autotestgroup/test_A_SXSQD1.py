#coding=UTF-8
# Author: cuichang
#   Date: 2018-07-11_14_10_52
# Modify the record:
from public.common import mytest
from public.pages import SubmitToBillPage
from time import strftime
from config import globalparam
import unittest
from public.common import publicfunction
from public.pages.billTestData import BillTestData
class test_A_SXSQD1(mytest.MyTest):
	"""测试单据-AutoTestGroup-A_事项申请单_01"""
	@unittest.skipUnless(globalparam.usecase_run_mode >= 1, "")
	def test_A_SXSQD1_01(self):
		"""测试单据-AutoTestGroup-A_事项申请单_01自动填单模式"""
		#初始化测试对象
		fsscTest = SubmitToBillPage.SubmitToBillPage(self.dr)
		#准备测试数据
		billName = "A_事项申请单_01"
		fillPerson = "填单用户001"
		approvalModel = "Auto"
		testCaseFile = "AutoTestGroup\A_事项申请单_01.xls"
		testCaseData = BillTestData(testCaseFile)
		#打开系统
		fsscTest.openSystem(globalparam.system_address)
		fsscTest.login(fillPerson)
		fsscTest.intoFillBillPage(billName)
		billNum = fsscTest.getBillNum()
		publicfunction.get_img(self.dr,billNum+"_"+strftime('%Y-%m-%d_%H_%M_%S')+".jpg")
		fsscTest.typeInputBillValue(testCaseData)
		publicfunction.get_img(self.dr, billNum + "_" + strftime('%Y-%m-%d_%H_%M_%S') + ".jpg")
		fsscTest.saveBill()
		fsscTest.switchToContentIframe()
		verifyResult = fsscTest.verifyBillValue(testCaseData)
		fsscTest.switch_to_iframe_out()
		self.assertTrue(verifyResult["verifyResult"],verifyResult["verifyMsg"])
		publicfunction.get_img(self.dr, billNum + "_" + strftime('%Y-%m-%d_%H_%M_%S') + ".jpg")
		nextApproveList = fsscTest.submissionBill()
		fsscTest.logoutSystem()
		if approvalModel == "Auto":
			fsscTest.handleBillAuto(nextApproveList, billNum, testCaseData)
		elif approvalModel == "Manual":
			fsscTest.handleBillManual(billNum, testCaseData)


	@unittest.skipUnless(globalparam.usecase_run_mode >= 1, "")
	def test_A_SXSQD1_02(self):
		"""测试单据-AutoTestGroup-A_事项申请单_01Manual模式"""
		#初始化测试对象
		fsscTest = SubmitToBillPage.SubmitToBillPage(self.dr)
		#准备测试数据
		billName = "A_事项申请单_01"
		fillPerson = "填单用户001"
		approvalModel = "Manual"
		testCaseFile = "AutoTestGroup\A_事项申请单_01.xls"
		testCaseData = BillTestData(testCaseFile)
		#打开系统
		fsscTest.openSystem(globalparam.system_address)
		fsscTest.login(fillPerson)
		fsscTest.intoFillBillPage(billName)
		billNum = fsscTest.getBillNum()
		publicfunction.get_img(self.dr, billNum + "_" + strftime('%Y-%m-%d_%H_%M_%S') + ".jpg")
		fsscTest.typeInputBillValue(testCaseData)
		publicfunction.get_img(self.dr, billNum + "_" + strftime('%Y-%m-%d_%H_%M_%S') + ".jpg")
		fsscTest.saveBill()
		fsscTest.switchToContentIframe()
		verifyResult = fsscTest.verifyBillValue(testCaseData)
		fsscTest.switch_to_iframe_out()
		self.assertTrue(verifyResult["verifyResult"],verifyResult["verifyMsg"])
		publicfunction.get_img(self.dr, billNum + "_" + strftime('%Y-%m-%d_%H_%M_%S') + ".jpg")
		nextApproveList = fsscTest.submissionBill()
		fsscTest.logoutSystem()
		if approvalModel == "Auto":
			fsscTest.handleBillAuto(nextApproveList, billNum, testCaseData)
		elif approvalModel == "Manual":
			fsscTest.handleBillManual(billNum, testCaseData)
