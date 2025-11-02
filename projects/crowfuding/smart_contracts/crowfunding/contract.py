from algopy import ARC4Contract, UInt64, GlobalState, Txn, Global, gtxn
from algopy.arc4 import abimethod, String, UInt64 as ARC4UInt64

class Crowdfunding(ARC4Contract):
   
    def __init__(self) -> None:
        # Track total donations received
        self.total_donations = GlobalState(UInt64)
        # Track number of donors
        self.donor_count = GlobalState(UInt64)
    
    @abimethod()
    def hello(self, name: String) -> String:
       
        return String.from_bytes(b"Hello, ") + name
    
    @abimethod()
    def donate(self, payment: gtxn.PaymentTransaction) -> String:
       
        # Verify payment is sent to this contract
        assert payment.receiver == Global.current_application_address, "Payment must be to this contract"
        
        # Verify amount is greater than 0
        assert payment.amount > 0, "Donation must be greater than 0"
        
        # Update total donations
        self.total_donations.value += payment.amount
        
        # Increment donor count
        self.donor_count.value += UInt64(1)
        
        return String.from_bytes(b"Thank you for your donation!")
    
    @abimethod()
    def get_total_donations(self) -> ARC4UInt64:
       
        return ARC4UInt64(self.total_donations.value)
    
    @abimethod()
    def get_donor_count(self) -> ARC4UInt64:
       
        return ARC4UInt64(self.donor_count.value)
    
    @abimethod()
    def get_donation_info(self) -> String:
      
        return String.from_bytes(b"Donation contract is active!")
