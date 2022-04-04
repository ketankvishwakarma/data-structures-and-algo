def sock_merchant(n, ar):
    # Write your code here
    socks_map = {}
    pair_count =0
    for idx, val in enumerate(ar):
        if val in socks_map:
            socks_map[val] = socks_map[val]+1
        else:
            socks_map[val] = 1
        if socks_map[val]%2==0:
            pair_count+=1   
    return pair_count


print(sock_merchant(9,[10, 20, 20, 10, 10, 30, 50 ,10, 20]))