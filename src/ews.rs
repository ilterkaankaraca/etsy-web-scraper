use reqwest;
pub async fn get_sales(link: &str) -> Result<String, reqwest::Error> {
{
    let html = reqwest::get(link).await?.text().await?;
    println!("12{:?}", html);
    Ok(html)
}
//   try:
//     request= requests.get(link)
//   except requests.exceptions.RequestException or ConnectionAbortedError:
//   request = requests.get(link)
//   htmlText = request.text
//   status = request.status_code
//   soup = BeautifulSoup(htmlText, 'html.parser')
//   if soup.body.find('span', attrs={'class': 'wt-text-caption wt-no-wrap'}) is not None:
//     sale_number = soup.body.find('span', attrs={'class': 'wt-text-caption wt-no-wrap'}).text[:-6].replace(',','')
//   elif soup.body.find('span', attrs={'class': 'wt-text-caption wt-no-wrap'}) is None or status[0]!='2':
//     sale_number = '-'
//   return sale_number

// def checkConnection(link : str):
//   while True: 
//     try:
//         requests.get(link)
//     except requests.exceptions.RequestException or ConnectionAbortedError:
//       continue
//     break
}
