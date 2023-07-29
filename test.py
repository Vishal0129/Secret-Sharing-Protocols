from SSS import SSS

def sss_test():
    secret = int(input("Enter the secret: "))
    shares = int(input("Enter the number of shares: "))
    threshold = int(input("Enter the threshold: "))
    sss = SSS(secret, shares, threshold)

    print("Shares: \n")
    sss_shares = sss.shares()
    print(sss_shares)
    for i in sss_shares.keys():
        print(i, ":", sss_shares[i])

    # print("Reconstructed secret: ", sss.reconstruct(sss.shares()))
    print("Input {sss.k} shares to reconstruct the secret: ")
    re_shares = dict()
    for i in range(sss.k):
        share_number = int(input("Enter the share number: "))
        share_value = int(input("Enter the share value: "))
        re_shares[share_number] = share_value 
    print(re_shares)
    print("Reconstructed secret: ", sss.reconstruct(re_shares))

def main():
    sss_test()

if __name__ == "__main__":
    main()