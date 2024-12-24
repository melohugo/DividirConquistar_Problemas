class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def mediana(lista):
            lista.sort()
            return lista[len(lista) // 2]

        def mediana_das_medianas(lista):
            if len(lista) <= 5:
                return mediana(lista)

            medianas = []

            for i in range(0, len(lista), 5):
                grupo = lista[i:i+5]
                grupo.sort()
                medianas.append(mediana(grupo))

            return mediana_das_medianas(medianas)

        def kth_largest(lista, k):
            pivo = mediana_das_medianas(lista)

            menores = [elemento for elemento in lista if elemento < pivo]
            iguais = [elemento for elemento in lista if elemento == pivo]
            maiores = [elemento for elemento in lista if elemento > pivo]

            if k <= len(maiores):
                return kth_largest(maiores, k)
            elif k <= len(maiores) + len(iguais):
                return pivo
            else:
                return kth_largest(menores, k - len(maiores) - len(iguais))

        return kth_largest(nums, k)
