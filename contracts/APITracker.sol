// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;

contract DuneAPITracker {
    struct APICalls {
        address caller;
        uint256 queryId;
    }

    mapping(uint256 => APICalls) public tracker;

    address public owner = address(0x4E2CC19317d23680AAfE52189491D12F890c3c02);

    event APICallMade(address caller, uint256 queryId);

    uint256 public calls = 0;

    uint256 public cpc = 100000000000000000;

    function apiCallTracker(uint256 queryId) public payable {
        require(msg.value >= cpc, "Need to pay sufficient amount to make a call!");

        calls += 1;
        tracker[calls] = APICalls(msg.sender, queryId);

        emit APICallMade(msg.sender, queryId);
    }

    function withdraw() public {
        require(msg.sender==owner, "Need to be owner to withdraw funds!");

        uint256 balance = address(this).balance;
        payable(owner).transfer(balance);

    }
}