# Error

Stderr: VBoxManage.exe: error: Not in a hypervisor partition (HVP=0) (VERR_NEM_NOT_AVAILABLE).
VBoxManage.exe: error: VT-x is disabled in the BIOS for all CPU modes (VERR_VMX_MSR_ALL_VMX_DISABLED)
VBoxManage.exe: error: Details: code E_FAIL (0x80004005), component ConsoleWrap, interface IConsole

## VT 활성화 에러
VT활성화 불가능한 상태인데(BIOS 접근 비밀번호를 모르는 상태) 어떻게 해야하는가..?
결국 본체를 뜯어서 CMOS 배터리를 초기화해주는 작업을 해주었다.. 
VT 활성화 완료...

## 스파크를 다루는 기술 실습(p116~p139)
$ spark-shell

#transByCustRDD 만들기
scala> val tranFile = sc.textFile("first-edition/ch04/ch04_data_transactions.txt")
scala> val tranData = tranFile.map(_.split("#"))

scala> val transByProd = tranData.map(tran => (tran(3).toInt, tran))
scala> val totalsByProd = transByProd.mapValues(t => t(5).toDouble).reduceByKey{case(tot1, tot2) => tot1 + tot2}

scala> val products = sc.textFile("firt-edition/ch04/ch04_data_products.txt").
    map(line => line.split("#")).
    map(p => (p(0).toInt, p))
    
val transByProd = tranData.map(tran => (tran(3).toInt, tran))
val totalsByProd = transByProd.mapValues(t => t(5).toDouble).
   reduceByKey{case(tot1, tot2) => tot1 + tot2}
    
scala> val totalsAndProds = totalsByProd.join(products)
scala> totalsAndProds.first()
scala> val totalsWithMissingProds = totalsByProd.rightOuterJoin(products)
scala> val missingProds = totalsWithMissingProds.filter(x => x._2._1 == None).map(x => x._2._2)
scala> missingProds.foreach(p => println(p.mkString(", ")))