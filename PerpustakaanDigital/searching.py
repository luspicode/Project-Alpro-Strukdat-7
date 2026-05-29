def linear_search(daftar_buku, keyword):

    keyword = keyword.lower()

    for buku in daftar_buku:

        if keyword in buku["judul"].lower():
            return buku

    return None

def binary_search(daftar_buku, keyword):

    low = 0
    high = len(daftar_buku) - 1

    keyword = keyword.lower()

    while low <= high:

        mid = (low + high) // 2

        judul_tengah = (
            daftar_buku[mid]["judul"]
            .lower()
        )
        
        if keyword == judul_tengah:
            return daftar_buku[mid]

        elif keyword > judul_tengah:
            low = mid + 1

        else:
            high = mid - 1

    return None
