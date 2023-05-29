//
//  main.swift
//  K번째수
//
//  Created by 예강이다 on 2023/05/28.
//

import Foundation

let array = [1, 5, 2, 6, 3, 7, 4]
let commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

var result = [Int]()

for i in 0..<commands.count {
    let startIdx = commands[i][0]
    let endIdx = commands[i][1]
    let findIdx = commands[i][2]
    
    let sortArr = array[startIdx-1...endIdx-1].sorted()
    let num = sortArr[findIdx-1]
    result.append(num)
}

print(result)
