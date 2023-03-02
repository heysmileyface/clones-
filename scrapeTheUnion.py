
import bs4
import requests
import selenium
import re
# Get the page
res = requests.get('https://www.stirlingstudentsunion.com/clubssocieties/societies/')

# Create a BeautifulSoup object
soup = bs4.BeautifulSoup(res.text, 'html.parser')
all_links = []
# Find the element the href in each list item
elems = soup.select('li a ')
#get all hrefs
for elem in elems:
    #only print if they contain "/clubssocieties/societies/"
    if "/clubssocieties/societies/" in elem.get('href'):
        #add to list
        all_links.append(elem.get('href'))
#remove duplicates
all_links = list(set(all_links))
# print(all_links)
print(len(all_links))


for link in all_links:
    if len(link) == 26:
        continue
    res = requests.get('https://www.stirlingstudentsunion.com' + link)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # get email by class 'msl_email'
    # print(link)
    name = soup.select('h1')[1].getText()
    print(name)
    #press "commitee" button
    res = requests.post('https://www.stirlingstudentsunion.com' + link, data={'committee': 'committee'})
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
    element = soup.find(id='ctl00_Main_groupedmemberlist_rptGroups_ctl00_rptGroupsItemised_ctl00_rptMembers_ctl01_bPerson_hlEmailAddress')
    element2 = soup.find(id='ctl00_groupedmemberlist_rptGroups_ctl00_rptGroupsItemised_ctl00_rptMembers_ctl01_bPerson_hlEmailAddress')
    element3 = soup.find(id='ctl00_groupedmemberlist_rptGroups_ctl00_rptGroupsItemised_ctl00_rptMembers_ctl01_bPerson_hlEmailAddress')
    
    if element:
        print(element.text)
    elif element2:
        print(element2.text)
    elif element3:
        print(element3.text)
    else:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
    soup = str(soup)
    name_pattern = re.compile(r'<dt><a\s+href="/profile/\d+/">(.+?)</a></dt>')
    match = name_pattern.search(soup)

    if match:
        name = match.group(1)
        print(name)

