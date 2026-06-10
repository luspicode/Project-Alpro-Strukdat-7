def linear_search(daftar_buku, keyword):

    keyword = keyword.lower()

    for buku in daftar_buku:

        if keyword in buku["judul"].lower():
            return buku

    return None
