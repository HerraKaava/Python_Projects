

def summa(luku: int):
    """
    Funktio laskee parametrina annetusta luvusta alaspäin (luku itse mukaan lukien) lukujen summan.
    """
    # Kun luku on 1, ei ole enää summattavia lukuja
    if luku <= 1:
        return luku

    # Rekursio
    return luku + summa(luku-1)


if __name__ == "__main__":
    print(summa(10))    # 55
    print(summa(5))     # 15
    