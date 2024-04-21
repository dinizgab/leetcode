package main

type Bucket [26]byte

func groupAnagrams(strs []string) [][]string {
    stringsBucket := map[Bucket][]string{}

	for _, value := range strs {
		charCounter := [26]byte{}
    
        for _, ch := range value {
            charCounter[ch - 'a'] += 1
        }
        stringsBucket[charCounter] = append(stringsBucket[charCounter], value)
	}

    result := [][]string{}
    for _, v := range stringsBucket {
        result = append(result, v)
    }

    return result
}
