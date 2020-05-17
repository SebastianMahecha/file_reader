from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from main.workers.utils import CommonsUtils
from main.workers.webdriver_helper import WebdriverHelper
from urllib.request import Request, urlopen
import sys, json, requests, nltk, re, time

class DocumentWorker:
	
	def run_worker(self, first_name, last_name):
		
		sites = []		
		driver_helper = WebdriverHelper("main/chromedriver/chromedriver")
		driver_helper.open_page("http://www.google.com")
		search = driver_helper.find_element_by_tag_attribute("input", "name", "q")
		
		
		search.send_keys(first_name+" "+last_name + " -site:pinterest.com -site:twitter.com -site:linkedin.com -site:facebook.com -site:instagram.com -site:youtube.com")
		search.submit()	
		
		more_options = driver_helper.find_elements_by_path('//span[@class="gL9Hy"]/a')
		if len(more_options) > 0:
			driver_helper.open_page(more_options[0].get_attribute("href"))
		more_options = driver_helper.find_elements_by_path('//a[@class="gL9Hy"]')
		if len(more_options) > 0:
			driver_helper.open_page(more_options[0].get_attribute("href"))
		results = driver_helper.find_elements_by_path('//div[@class="r"]/a')
 
		i = 0
		links = []
		for element in results:
			
			try:
				link_href = element.get_attribute("href")				
				
				if ".pdf" in link_href or ".docx" in link_href or ".doc" in link_href or ".xlsx" in link_href or ".xls" in link_href or "download" in link_href:
					pass
				else:
					links.append(link_href)
					
			except:
				print("link raro")

		for link in links:
			
			driver_helper.open_page(link)
			elements = driver_helper.find_elements_by_path('//*')
			glossary = ""
			limit = 1000
			time_limit = 180
			start = time.time()
			for element in elements:						
				
				try:
					text = re.sub('^[a-zA-Z0-9\\-\\s]+$', ' ', element.text)
				except:
					text = ""
				
				text = text.replace("  ", " ")				
				text = text.strip()				
				text = text.replace(" ", ",")				
				text = text.replace("\n", ",")				
				if text != "":					
					glossary +=  ","+text
			
				limit -= 1
				if limit <= 0 or time.time() > start + time_limit:
					break
			if glossary.strip() != "":
				sites.append({
					"url": link,
					"glossary": glossary,
				})
				i+=1			
				if i >= 3:
					break
			
		driver_helper.close_page()
		return sites
	