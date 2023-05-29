//
//  main.swift
//  예산
//
//  Created by 예강이다 on 2023/05/20.
//

import Foundation

let d = [100]
let budget = 101

var dArr = d.sorted()
var bud = budget
var result = 0

for i in 0..<d.count {
    if bud - dArr[i] >= 0{
        bud -= dArr[i]
        result += 1
    } else {
        break
    }
}

print(result)
