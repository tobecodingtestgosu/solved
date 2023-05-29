//
//  main.swift
//  1920_수 찾기
//
//  Created by 예강이다 on 2023/05/25.
//

import Foundation

let N = Int(readLine()!)!
var arr1 = readLine()!.split(separator: " ").map{ Int($0)! }

let M = Int(readLine()!)!
var arr2 = readLine()!.split(separator: " ").map{ Int($0)! }

arr1.sort()

func binarySearch(_ arr: [Int], _ target: Int) -> Int {
    var start = 0
    var end = arr.count - 1
    
    while start <= end {
        let mid = (start + end) / 2
        if arr1[mid] == target {
            return 1
        } else if arr1[mid] > target {
            end = mid - 1
        } else if arr1[mid] < target {
            start = mid + 1
        }
    }
    return 0
}

for i in 0..<M {
    print(binarySearch(arr1, arr2[i]))
}
