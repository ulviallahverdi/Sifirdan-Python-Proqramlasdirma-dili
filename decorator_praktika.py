def ekstra(funk):
    def wrapper(reqemler):
        cutlerin_cemi = 0
        cut_reqemler = 0
        teklerin_cemi = 0
        tek_ededler = 0
 
        for reqem in reqemler:
 
            if (reqem % 2 == 0):
 
                cutlerin_cemi += reqem
                cut_reqemler += 1
            else:
                teklerin_cemi += reqem
                tek_ededler += 1
        print("Tek ededlerin ortalamasi:",teklerin_cemi / tek_ededler)
        print("Cut ededlerin ortalamasi:",cutlerin_cemi/ cut_reqemler)
        funk(reqemler)
    return wrapper

@ekstra
def ortalamatap(reqemler):
    cem = 0
    for reqem in reqemler:
        cem += reqem
    print("Umumi Ortalama:",cem/len(reqemler))
ortalamatap([1,2,3,4,34,60,63,32,100,105])
