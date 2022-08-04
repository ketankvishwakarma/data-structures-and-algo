
def find_roam(A,B):
    print("*************************")
    city_road_map = {}
    roam_count = {}
    city_of_rome = -9
    for i in range(len(A)):
        city_road_map[A[i]]=B[i]
        if B[i] in roam_count.keys():
           roam_count[B[i]] += 1
        else:
            roam_count[B[i]] = 1
        city_of_rome = max(city_of_rome,roam_count[B[i]])  
    print("m {}".format(city_road_map))
    print("roam_count {}".format(roam_count))
    print("max_raod {}".format(city_of_rome))
    if len(roam_count)==1:
        return list(roam_count.keys())[0]
    if city_of_rome in roam_count.keys():
        del roam_count[city_of_rome]
    print("roam_count {}".format(roam_count))

    for x in roam_count:
        print("x={} and max_road={} and m={} ".format(x,city_of_rome,city_road_map))
        if x not in city_road_map or city_road_map[x] != city_of_rome:
                return -1
    return city_of_rome


if __name__ =="__main__":
    a = [0,1,2,4,5]
    b = [2,3,3,3,2]
    #print(find_roam(a,b))
    a = [2,3,3,4]
    b = [1,1,0,0]
    print(find_roam(a,b))
    a = [1,2,3]
    b = [0,0,0]
    #print(find_roam(a,b))