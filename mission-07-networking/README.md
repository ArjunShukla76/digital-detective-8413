# Mission 7: Networking

## 1. Task / objective
Learn about LAN, MAN, WAN, DNS, and how a browser communicates with a website. Practise using `ping` and `nslookup`.

## 2. Work completed
- Compared LAN, MAN, and WAN.
- Used `ping` to check whether `example.com` responded.
- Used `nslookup` to look up `example.com` through a DNS server.
- Described the steps a browser takes to load a website.

## 3. Commands / tools used
- `ping -c 4 example.com`
- `nslookup example.com 8.8.8.8`
- Terminal

## 4. My understanding
A LAN connects devices in a small area, such as a home or school. A MAN covers a larger area, such as a city. A WAN connects networks across large distances; the internet is a WAN.

DNS looks up the IP address associated with a domain name. `nslookup` asks a DNS server for that information. `ping` sends test messages to check whether a host responds and how long replies take.

When I visit a website, the browser looks up the domain with DNS, connects to the server, sends an HTTP or HTTPS request, receives the response, and displays the page.

## 5. Difficulties faced
I needed to distinguish a DNS lookup from a connectivity test.

## 6. How I resolved them
I compared the commands: `nslookup` looked up the domain, while `ping` tested for replies. All four ping packets received replies.

## 7. Evidence / files
- `README.md`
- `ping -c 4 example.com`: 4 packets received, no packet loss
- `nslookup example.com 8.8.8.8`: returned DNS results
- IP addresses omitted from this README

## 8. Commit details
Commit message: Explain networking concepts and website communication

