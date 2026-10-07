# PAYSIM : Real-Time Wallet & AI Fraud Detection Platform

# 1. Project Overview

### PaySim is a sandbox payment and wallet platform that allows users to create accounts, manage demo wallets, perform simulated P2P transactions, and experience a production-style payment processing system with real-time fraud detection.

<p> This system is work on demo money not real money. </p>

## Purpose of System
<ul>
    <li>Backend Engineering</li>
    <li>Fintech architecture</li>
    <li>Distributed ststems</li>
    <li>AI fraud detection</li>
    <li>Payment workflows</li>
    <li>Security</li>
    <li>Scalability</li>
</ul>


# 2. Goals

## Primary Goals
<ol>
    <li>Users can create sandbox accounts.</li>
    <li>Users can create/manage demo wallets.</li>
    <li>Users can add demo funds.</li>
    <li>Users can transfer demo funds.</li>
    <li>Every transfer is recorded through a ledger.</li>
    <li>Concurrent transfer must not cause incorrect balances.</li>
    <li>Duplicate request must not create duplicate transactions.</li>
    <li>Transactions are evaluated for fraud risk.</li>
    <li>Suspicious transactions can be blocked/reviewed.</li>
    <li>Users can view transaction history.</li>
    <li>Developers can interact with the sandbox through APIs.</li>
</ol>

## AI Goals
<ol>
    <li>Real-time fraud scoring.</li>
    <li>Rule-based risk detection.</li>
    <li>ML-based risk prediction.</li>
    <li>LLM-generated human-readable explanation.</li>
</ol>


# 3. Non-Goals
<ol>
    <li>Real bank integration.</li>
    <li>Real UPI payments.</li>
    <li>Real card payments.</li>
    <li>Real money deposits.</li>
    <li>Real withdrawals.</li>
    <li>Real KYC verification.</li>
    <li>Real currency settlement.</li>
    <li>Actual bank network integration.</li>
    <li>Production financial compliance.</li>
</ol>

# 4. Scope
## Account
<ul>
    <li>Registration</li>
    <li>Login</li>
    <li>Logout</li>
    <li>Profile</li>
    <li>Password management</li>
</ul>

## Wallet
<ul>
    <li>Create wallet</li>
    <li>View balance</li>
    <li>Demo Top-Up</li>
    <li>Wallet history</li>
</ul>

## Transfers
<ul>
    <li>P2P transfer</li>
    <li>Transaction status</li>
    <li>Transaction history</li>
    <li>Transaction receipt</li>
</ul>

## Financial Correctness
<ul>
    <li>Double-entry ledger</li>
    <li>Atomic transactions</li>
    <li>Concurrency control</li>
    <li>Idempotency</li>
</ul>

## Security
<ul>
    <li>JWT</li>
    <li>Refresh token</li>
    <li>Rate limiting</li>
    <li>2FA</li>
    <li>Device/session management</li>
    <li>Audit logs</li>
</ul>

## Fraud
<ul>
    <li>Rule engine</li>
    <li>Velocity checks</li>
    <li>Risk scoring</li>
    <li>ML model</li>
    <li>Fraud explanation</li>
</ul>

## Developer Platform
<ul>
    <li>API keys</li>
    <li>Webhooks</li>
    <li>Sandbox API</li>
</ul>
