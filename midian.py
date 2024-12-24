class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        def merge_arrays(ent1, ent2):
            Vmerjado = []
            i, j = 0, 0

            while i < len(ent1) and j < len(ent2):
                if ent1[i] < ent2[j]:
                    Vmerjado.append(ent1[i])
                    i += 1
                else:
                    Vmerjado.append(ent2[j])
                    j += 1

            while i < len(ent1):
                Vmerjado.append(ent1[i])
                i += 1

            while j < len(ent2):
                Vmerjado.append(ent2[j])
                j += 1

            return Vmerjado

        Vmerjado = merge_arrays(nums1, nums2)
        n = len(Vmerjado)

        if n % 2 == 0:
            return (Vmerjado[n // 2 - 1] + Vmerjado[n // 2]) / 2.0
        else:
            return Vmerjado[n // 2]
