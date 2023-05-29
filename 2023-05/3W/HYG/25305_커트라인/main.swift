//
//  main.swift
//  25305_커트라인
//
//  Created by 예강이다 on 2023/05/20.
//

import Foundation

let NM = readLine()!.split(separator: " ").map{ Int($0)! }
let N = NM[0]
let k = NM[1]

var arr = Array(repeating: 0, count: N)

let input = readLine()!.split(separator: " ").map{ Int($0)! }
for i in 0..<N {
    arr[i] = input[i]
}

let result = arr.sorted(by: >)

print(result[k-1])
