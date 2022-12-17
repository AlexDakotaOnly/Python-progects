import urllib.request as urllib


def main(input_url):
    print("Checking connectivity...")

    response = urllib.urlopen(input_url)
    print("Connected to url", input_url, "succesfully")
    print("The response code was:", response.getcode())


print("This is a site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")

main(input_url)





