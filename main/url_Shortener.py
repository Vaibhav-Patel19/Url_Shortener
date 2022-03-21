import pyshorteners as sh

s = sh.Shortener()

link = "https://www.linkedin.com/in/vaibhavpatel19/"

print(s.tinyurl.short(link))