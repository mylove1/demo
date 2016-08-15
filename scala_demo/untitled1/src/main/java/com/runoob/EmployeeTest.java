package com.runoob;
import java.io.*;

/**
 * Created by Nailcui on 2016/8/14.
 */
public class EmployeeTest {

    public static void main(String args[]){
        Employee empOne = new Employee("Gao");
        Employee empTwo = new Employee("Cui");

        // 调用这两个对象的成员方法
        empOne.empAge(26);
        empOne.empDesignation("Gao PingAn CEO");
        empOne.empSalary(10000);
        empOne.printEmployee();

        empTwo.empAge(21);
        empTwo.empDesignation("XZS Spider");
        empTwo.empSalary(20000);
        empTwo.printEmployee();
    }

}
