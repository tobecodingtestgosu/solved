//
//  main.swift
//  모의고사
//
//  Created by 예강이다 on 2023/05/28.
//

import Foundation

let answers = [1,3,2,4,2]

let student1 = [1,2,3,4,5]
let student2 = [2,1,2,3,2,4,2,5]
let student3 = [3,3,1,1,2,2,4,4,5,5]

var dic = [Int: Int]()

for i in 0..<answers.count {
    if answers[i] == student1[i%student1.count] {
        dic[1] = (dic[1] ?? 0) + 1
    }
    if answers[i] == student2[i%student2.count] {
        dic[2] = (dic[2] ?? 0) + 1
    }
    if answers[i] == student3[i%student3.count] {
        dic[3] = (dic[3] ?? 0) + 1
    }
}

let max = dic.values.max()!

let result = dic.filter{ $0.value == max }.keys.sorted()

print(result)
