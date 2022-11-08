//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.17;
import "OpenZeppelin/openzeppelin-contracts@4.7.3/contracts/utils/Strings.sol";


contract Shop {
  address public merchant = address(0x66aB6D9362d4F35596279692F0251Db635165871);
  address buyer;
  uint256 public price;

  constructor(){
    require(msg.sender == merchant);
    price = 0;
  }

  function Pricing(uint256 _price) public
  {
    require(msg.sender == merchant);
    price = _price;
  } 

  function Pay() payable public{
    uint256 gasPrice = block.gaslimit * tx.gasprice;
    uint256 finalPrice = gasPrice + price;
  
    require(msg.value >= finalPrice ,string.concat('Please send full Money ',Strings.toString(finalPrice/1 ether)," Ether. Money sent ", Strings.toString(msg.value)));
  }
  
  function Withdraw() public
  {
    payable(merchant).transfer(address(this).balance);
  }  
}