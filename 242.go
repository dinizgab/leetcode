package main

func isAnagram(s string, t string) bool {
    mapS := map[byte]int{}
    mapT := map[byte]int{}


    if len(s) != len(t) {
        return false
    }

    for i := range(len(s)) {
        mapS[s[i]] += 1
        mapT[t[i]] += 1
    }

    for k, _ := range(mapS) {
        if mapS[k] != mapT[k] {
            return false
        }
    }

    return true
}
