//
//  main.swift
//  18870_좌표 압축
//
//  Created by 예강이다 on 2023/05/24.
//

import Foundation

let N = Int(readLine()!)!
var num = Set<Int>()
let X = readLine()!.split(separator: " ").map{ Int($0)! }

for i in 1...N {
    num.insert(X[i-1])
}

let sortedNum = num.sorted(by: <)

func binarySearch<T: Comparable> (array: [T], key: T) -> Int? {
    var lowerBound = 0
    var upperBound = array.count
    
    while lowerBound < upperBound {
        let midIndex = lowerBound + (upperBound - lowerBound) / 2
        
        if array[midIndex] == key {
            return midIndex
        } else  if array[midIndex] < key {
            lowerBound = midIndex + 1
        } else {
            upperBound = midIndex
        }
    }
    return nil
}

for i in X {
    print("\(binarySearch(array: sortedNum, key: i)!) ", terminator: "")
}
