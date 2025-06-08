#!/usr/bin/env python
# coding: utf-8

# In[20]:


# Q1.
#계좌 개설: 은행 이름, 예금주, 계좌번호, 잔액  
# 생성자: 예금주, 초기 잔액

import random


class Account:
    bank = 'SC은행'
    account_count = 0   # 지금까지 만든 계좌 수            
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.account_number = self.generate_account_number()
        
        self.deposit_count = 0
        self.deposit_list = []
        
        self.withdraw_list = []
        
        Account.account_count += 1                        
    
    def generate_account_number(self):
        f = random.randint(100,999)
        s = random.randint(10,99)
        t = random.randint(100000,999999)
        return f"{f}-{s}-{t}"
    
    @classmethod
    def get_account_num(cls):
        print(f"총 계좌 개수: {cls.account_count}")
        
    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            self.deposit_count += 1
            self.deposit_list.append(amount)
            
            if self.deposit_count % 5 == 0:
                interest = self.balance * 0.01
                self.balance += interest
                
            print(f"{amount}원 입금되었습니다. 잔액: {self.balance:,}원")
        else:
            print("입금은 1원 이상만 가능합니다.")
        
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액이 부족합니다.")
        
        else:
            self.balance -= amount
            self.withdraw_list.append(amount)
            print(f"{amount}원 출금 되었습니다. 잔액: {self.balance:,}원")
            
            
    def display_info(self):
        print(f"은행이름: {Account.bank}, 예금주: {self.owner}, 계좌번호: {self.account_number}, 잔고: {self.balance:,}")
              
              
    def deposit_history(self):
              print(f"[입금 내역] {self.deposit_list}")
              
    def withdraw_history(self):
              print(f"[출금 내역] {self.withdraw_list}")
 


# In[21]:


a = Account("서민영", 1000000)
b = Account("강아지", 50000)
c = Account("고양이", 30000)

accounts = [a, b, c]


# In[22]:


for i in accounts:
    if i.balance >= 1000000:
        i.display_info()


# In[23]:


a.deposit(50000)


# In[24]:


a.withdraw(30000)


# In[32]:


b.deposit(1000)


# In[29]:


#Q2. RPG게임 만들기


class Character:
    def __init__(self, name, level, health, attack, defense):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense
        
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
        true_damage = damage - self.defense
        
        if true_damage > 0:
            self.health -= true_damage
            print(f"{self.name}이 {true_damage}의 피해를 입었습니다. 현재 체력: {self.hp}")
        else:
            print(f"{self.name}이 방어력으로 피해를 막았습니다.)
                  
            
    
    def attack_target(self, target):
                  damage = random.randint(1, self.attack)
                  print(f"{self.name}가 {target.name}에게 {damage}를 입혔습니다.")
#                   target.take_damage(damage)
                  
                  
                  
class Player(Character):
                  def __init__ (self, name):
                  super().__init__(name, level=1, health=100, attack=25, defense=5)
                  self.exp = 0   # 경험치 속성 추가
                  
                  def gain_experience(self,amount):
                  self.exp += amount
                  print(f"{self.name}이 {amount} 경험치를 획득하였습니다. (현재 경험치: {self.exp})")
                  
                  def level_up(self):
                  if self.exp >= 50:
                  self.exp -= 50
                  self.level += 1
                  self.attack += 10
                  self.defense += 5
                  print(f"레벨 업! {self.name}은 레벨 {self.level}이 되었습니다!")
                  
                  
class Monster(Character):
                  def __init__ (self, name, init):
                  health = random.randint(10, 30) * level
                  attack = random.randint(5, 20) * level
                  defense = random.randint(1, 5) * level
                  super(),__init__(name, level, health, attack, defense)
                  
                  
                  
#생명력이 0이 되기 전까지 계에에에속 싸움
                  
def battle(player, monster):
                  while player.is_alive() and monster.is_alive():
                  player.attack_target(monster)
                  if monster.is_alive():
                  monster.attack_target(player)
                  
                  if player.is_alive():
                  print(f"전투 승리!")
                  gained_exp = monster.level * 20
                  
                  


# In[ ]:




