//
//  main.swift
//  두 개 뽑아서 더하기
//
//  Created by 예강이다 on 2023/05/23.
//

import Foundation

let numbers = [2,1,3,4,1]
var numArr = [Int]()
var num = numbers.sorted()

for i in 0..<num.count {
    for j in i+1..<num.count {
        numArr.append(num[i]+num[j])
    }
}
print(Array(Set(numArr)).sorted())
