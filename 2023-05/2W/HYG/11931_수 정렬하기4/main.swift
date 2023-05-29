//
//  main.swift
//  11931_수 정렬하기4
//
//  Created by 예강이다 on 2023/05/15.
//

import Foundation

let N = Int(readLine()!)!
var arr = Array(repeating: false, count: 2000001)
var str = ""

for _ in 1...N {
    let num = Int(readLine()!)!
    arr[num + 1000000] = true
}

for i in 20000000..<1 {
    if arr[i] == true {
        str += "\(i-1000000)\n"
    }
}

print(str)
