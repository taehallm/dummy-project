import requests


def main():
    response = requests.get("https://httpbin.org/ip")
    print("내 IP 주소는:", response.json()["origin"])


if __name__ == "__main__":
    main()
