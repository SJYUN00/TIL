import requests
import bs4

url = 'https://movie.naver.com/movie/point/af/list.naver'
response = requests.get(url)
html = response.text
review = bs4.BeautifulSoup(html)

# 리뷰만 확인
search = {
  'class':'title'
}
td_elements = review.find_all('td', attrs=search)

for element in td_elements:
  title = element.find('a').text
  score = element.find('em').text
  r = element.text.split('\n')[5]
  print(f'영화제목: {title}')
  print(f'평점: {score}')
  print(f'리뷰: {r}')

  