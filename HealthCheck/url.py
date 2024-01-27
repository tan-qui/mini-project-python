try:
  from bs4 import BeautifulSoup
  from selenium import webdriver
  from datetime import datetime
  import time

  current_date = datetime.now()
  print("=========================================Start=========================================\n")

  is_loop = True
  env_check = ""
  while is_loop:
    env_check = input(f"Bạn muốn check: dev/live ? ")
    if(env_check in "dev" or env_check in "live"):
      is_loop = False

  version_input = input(f"Nhập gần đúng version muốn check (ví dụ: {current_date.strftime('%Y/%m/%d')}) ")

  # 2024/01/11
  live_urls = [
    {"name": "vending-admin-company-fe", "url": "https://vending-admin-company.kootoro.com"},
    {"name": "vending-admin-fe", "url": "https://vending-admin.kootoro.com"},
    {"name": "vending-partner-fe", "url": "https://vending-partner.kootoro.com"},
    {"name": "vending-torogo", "url": "https://vending-torogo.kootoro.com/health-check"},
    {"name": "vending-torogo-pilot", "url": "https://vending-torogo-pilot.kootoro.com/health-check"},
    {"name": "vending-admin-company2", "url": "https://vending-admin-company2.kootoro.com/Api/HealthCheck/HealthCheckAuto"},
    {"name": "vending-admin-company-api", "url": "https://vending-admin-company-api.kootoro.com/HealthCheckAuto"},
    {"name": "vending-admin-api", "url": "https://vending-admin-api.kootoro.com/HealthCheckAuto"},
    {"name": "vending-tracking-api", "url": "https://vending-tracking-api.kootoro.com/HealthCheckAuto"},
    {"name": "vending-customer-api", "url": "https://vending-customer-api.kootoro.com/HealthCheckAuto"},
    {"name": "vending-partner-api", "url": "https://vending-partner-api.kootoro.com/HealthCheckAuto"},
    {"name": "vending-payment-service", "url": "https://vending-payment-service.kootoro.com/HealthCheckAuto"},
    # {"name": "vending-monitor-api", "url": "https://vending-monitor-api.kootoro.com/HealthCheckAuto"},
    # {"name": "vending-report-api", "url": "https://vending-report-api.kootoro.com/HealthCheckAuto"},
  ]
  dev_urls = [

  ]
  urls = dev_urls if(env_check in "dev") else live_urls

  if(len(urls) == 0):
    print("Không tìm thấy url")
    print("\n=========================================End=========================================")
    time.sleep(2)
    quit()

  lstCheckVersion = []
  driver = webdriver.Chrome()
  for item in urls:
    driver.get(item["url"])
    soup = BeautifulSoup(driver.page_source, "html.parser")
    name = item["name"]
    content_version=""
    match name:
      case "vending-admin-company-fe":
        content_version = soup.script.get_text()
      case "vending-admin-fe":
        content_version = soup.script.get_text()
      case "vending-partner-fe":
        content_version = soup.script.get_text()
      case "vending-torogo-pilot":
        content_version = soup.p.get_text()
      case "vending-torogo":
        content_version = soup.p.get_text()
      case "vending-admin-company2":
        content_version = soup.pre.get_text()
      case "vending-admin-company-api":
        content_version = soup.pre.get_text()
      case "vending-admin-api":
        content_version = soup.pre.get_text()
      case "vending-monitor-api":
        content_version = soup.pre.get_text()
      case "vending-tracking-api":
        content_version = soup.pre.get_text()
      case "vending-customer-api":
        content_version = soup.pre.get_text()
      case "vending-partner-api":
        content_version = soup.pre.get_text()
      case "vending-payment-service":
        content_version = soup.pre.get_text()
      case "vending-report-api":
        content_version = soup.pre.get_text()
    # # Compare with verizon
    if version_input in content_version:
      new = {
        "name": item["name"],
        "url": item["url"],
        "status": "✅",
        "version": content_version
      }
      lstCheckVersion.append(new)
    else:
      old = {
        "name": item["name"],
        "url": item["url"],
        "status": "🔴",
        "version": content_version
      }
      lstCheckVersion.append(old)
  # Converrt aray to string 
  data_to_write = '\n'.join(map(str, lstCheckVersion))
  with open("health-check.txt", "w", encoding="utf-8") as file:
          file.write(data_to_write + '\n')
          
  print("Xem kết quả ở file health-check.txt cùng cấp thư mục")
  print("\n=========================================End=========================================")
  time.sleep(3)
  quit()
except Exception as bug:
  print(bug)
  print("\n=========================================End=========================================")
  time.sleep(10)
  quit()
