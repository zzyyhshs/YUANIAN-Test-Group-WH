#coding=UTF-8
# Author: hsy
#   Date: 2018-08-06_15_45_52
# Modify the record:
from public.common import mytest
from public.pages import SubmitToBillPage
from time import strftime
from config import globalparam
import unittest
from public.common import publicfunction
from public.pages.billTestData import BillTestData


class test_DBZ_BXDW1(mytest.MyTest):
	"""测试单据-费用报销组（多币种）-8.03-报销单-无申请"""

	@unittest.skipUnless(globalparam.usecase_run_mode >= 1, "")  # @unittest.skipUnless(True or Flase, "")
	def test_DBZ_BXDW1_01(self):
		"""测试单据-费用报销组（多币种）-8.03-报销单-无申请-本位币为人民币-无冲销"""
		#初始化测试对象
		fsscTest = SubmitToBillPage.SubmitToBillPage(self.dr)  # self.dr 从父类获取 父类当中封装了测试开始setUp，结束tearDown
		#准备测试数据
		billName = "8.03-报销单-无申请"
		fillPerson = "填单用户001"
		# 测试模式
		approvalModel = "Auto"
		testCaseFile = "费用报销组（多币种）\\8.03-报销单-无申请-01.xls"  # excel表路径
		# 创建一个对象，对象的属性分别是excel表的每一列数据
		testCaseData = BillTestData(testCaseFile)
		#打开系统
		fsscTest.openSystem(globalparam.system_address)  # globalparam.system_address： url
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
	def test_DBZ_BXDW1_02(self):
		"""测试单据-费用报销组（多币种）-8.03-报销单-无申请-本位币为美元-无冲销"""
		# 初始化测试对象
		fsscTest = SubmitToBillPage.SubmitToBillPage(self.dr)
		# 准备测试数据
		billName = "8.03-报销单-无申请"
		fillPerson = "填单用户007"
		approvalModel = "Auto"
		testCaseFile = "费用报销组（多币种）\\8.03-报销单-无申请-02.xls"
		testCaseData = BillTestData(testCaseFile)
		# 打开系统
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

	@unittest.skipUnless(globalparam.usecase_run_mode >= 1, "")
	def test_DBZ_BXDW1_03(self):
		"""测试单据-费用报销组（多币种）-8.03-报销单-无申请-本位币为人民币-明细区币种不一致"""
		#初始化测试对象
		fsscTest = SubmitToBillPage.SubmitToBillPage(self.dr)
		#准备测试数据
		billName = "8.03-报销单-无申请"
		fillPerson = "填单用户001"
		approvalModel = "Auto"
		testCaseFile = "费用报销组（多币种）\\8.03-报销单-无申请-03.xls"
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
		fsscTest.clickBillSubmit()
		fsscTest.windowAssertContain("币种必须一致", "币种未校验成功")
		fsscTest.logoutSystem()

	@unittest.skipUnless(globalparam.usecase_run_mode >= 1, "")
	def test_DBZ_BXDW1_04(self):
		"""测试单据-费用报销组（多币种）-8.03-报销单-无申请-本位币为美元-明细区币种不一致"""
		# 初始化测试对象
		fsscTest = SubmitToBillPage.SubmitToBillPage(self.dr)
		# 准备测试数据
		billName = "8.03-报销单-无申请"
		fillPerson = "填单用户007"
		approvalModel = "Auto"
		testCaseFile = "费用报销组（多币种）\\8.03-报销单-无申请-04.xls"
		testCaseData = BillTestData(testCaseFile)
		# 打开系统
		fsscTest.openSystem(globalparam.system_address)
		fsscTest.login(fillPerson)
		fsscTest.intoFillBillPage(billName)
		billNum = fsscTest.getBillNum()
		publicfunction.get_img(self.dr, billNum + "_" + strftime('%Y-%m-%d_%H_%M_%S') + ".jpg")
		fsscTest.typeInputBillValue(testCaseData)
		publicfunction.get_img(self.dr, billNum + "_" + strftime('%Y-%m-%d_%H_%M_%S') + ".jpg")
		fsscTest.saveBill()
		fsscTest.clickBillSubmit()
		fsscTest.windowAssertContain("币种必须一致", "币种未校验成功")
		fsscTest.logoutSystem()

	@unittest.skipUnless(globalparam.usecase_run_mode >= 1, "")
	def test_DBZ_BXDW1_05(self):
		"""测试单据-费用报销组（多币种）-8.03-报销单-无申请-本位币为人民币-币种一致"""
		#初始化测试对象
		fsscTest = SubmitToBillPage.SubmitToBillPage(self.dr)
		#准备测试数据
		billName = "8.03-报销单-无申请"
		fillPerson = "填单用户001"
		approvalModel = "Auto"
		testCaseFile = "费用报销组（多币种）\\8.03-报销单-无申请-05.xls"
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
	def test_DBZ_BXDW1_06(self):
		"""测试单据-费用报销组（多币种）-8.03-报销单-无申请-本位币为美元-币种一致"""
		#初始化测试对象
		fsscTest = SubmitToBillPage.SubmitToBillPage(self.dr)
		#准备测试数据
		billName = "8.03-报销单-无申请"
		fillPerson = "填单用户007"
		approvalModel = "Auto"
		testCaseFile = "费用报销组（多币种）\\8.03-报销单-无申请-06.xls"
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

