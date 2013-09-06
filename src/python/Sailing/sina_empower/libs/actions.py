# -*- coding: utf8 -*-
import sys
import time
import logging

class SinaBatchEmpower(object):
	def __init__(self, ):
		self.logger = logging.getLogger("click")
		
	def __call__(self, client, api, **kw):
		"""
		client -- 
		client
		api --        
		"""
		self.client = client
		self.driver = client.driver
		tid = kw['tid']
		username = kw['username']
		pw = kw['password']
		url = "http://www.zaol.cn/weibo/login.php?tid="+tid
		self.logger.info("============ start for sales  ============")
		self.logger.info('tid : %s  username: %s     password:%s  url:%s' %(tid, username, pw, url))
		self.open_empower_url(url)
		self.sina_empower(client, username, pw)
		self.logger.info("============ end for sales ============")
	
	def open_empower_url(self, url):
		self.logger.info("start open: %s" %(url))
		self.client.driver.get(url)
		time.sleep(3)
	def sina_empower(self, client, username, pw):
		userid = client.e("#userId")
		userid.send_keys(username)
		time.sleep(1)
		
		passwd = client.e("#passwd")
		passwd.send_keys(pw)
		time.sleep(1)
		
		
		submit = client.e(".WB_btn_login.formbtn_01")
		submit.click()
		time.sleep(3)
		
		try:
			codeinput = client.e(".WB_iptxt.oauth_form_input.oauth_form_code")
			full_screen_path = client.real_path("screen.png")
			captcha_path = client.real_path("captcha.png")
			for i in range(3):
				code = _get_captcha_code(driver,{'x':0,'y':0},full_screen_path, captcha_path)
				if code is None:
					break;
				#codeinput = client.e(".WB_iptxt.oauth_form_input.oauth_form_code")
				codeinput.send_key(code)
		except:
			pass
		
		for i in range(3):
			try:
				conect = client.e(".WB_btn_link.formbtn_01")
				connect.click()
				time.sleep(1)
			except:
				pass

	def _get_captcha_code(self, driver, p, full_screen_path, captcha_path):
		
		try:
			verifyshow = driver.find_element_by_css_selector(".check-code-img")
		except:
			print "Not found vrify code"
			return None
		
		driver.get_screenshot_as_file(full_screen_path)	
		vp = verifyshow.location
		s = verifyshow.size
		
		#box = (left, top, left+width, top+height)
		left = p['x'] + vp ['x']
		top = p['y'] + vp['y']
		new_box = (int(left), int(top), int(left + s['width']), int(top + s['height']))
			
		self.save_screenshot_img(full_screen_path, captcha_path, new_box)
		
		from sailing.webrobot.captcha import get_captcha

		print "starting get captcha: %s" % (captcha_path, )		
		data = get_captcha(captcha_path, )
		print "captcha response:%s" % str(data)
	
		if data['status'] == 'ok':
			code = data['captcha']
			return code
		
		return None
		
	def save_screenshot_img(self, input_path, out_path, box):
		from PIL import Image
		
		# size is width/height
		img = Image.open(input_path)
		#box = (2407, 804, 71, 796)
		area = img.crop(box)	
		area.save(out_path, 'png')
		#img.close()
		pass


