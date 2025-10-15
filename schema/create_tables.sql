-- Create Customer table
CREATE TABLE Customers (
    customer_id INTEGER,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    account_type TEXT NOT NULL,
    PRIMARY KEY (customer_id)
);

-- Create Agent table
CREATE TABLE Agents (
    agent_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    role TEXT NOT NULL,
    PRIMARY KEY (agent_id)
);

-- Create Ticket table
CREATE TABLE Tickets (
    ticket_id INTEGER,
    customer_id INTEGER NOT NULL,
    agent_id INTEGER NOT NULL,
    category TEXT NOT NULL,
    priority TEXT NOT NULL,
    status TEXT NOT NULL,
    created_at DATETIME NOT NULL, 
    first_response_at DATETIME,
    resolve_at DATETIME, 
    escalated_flag INTEGER NOT NULL DEFAULT 0,
    reopen_count INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (ticket_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (agent_id) REFERENCES Agents(agent_id)
);

-- Create escaltions table
CREATE TABLE Escalations (
    escalation_id INTEGER,
    ticket_id INTEGER NOT NULL,
    level INTEGER NOT NULL,
    handled_by INTEGER NOT NULL,
    escalation_date DATETIME NOT NULL,
    PRIMARY KEY (escalation_id),
    FOREIGN KEY (ticket_id) REFERENCES Tickets(ticket_id),
    FOREIGN KEY (handled_by) REFERENCES Tickets(agent_id)
);

-- Include a couple indexes although not strictly neccessary due to small scale of database
CREATE INDEX idx_tickets_agent ON Tickets(agent_id);
CREATE INDEX idx_tickets_customer ON Tickets(customer_id);
CREATE INDEX idx_tickets_cat_pri ON Tickets(category, priority);