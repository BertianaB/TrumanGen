
"""

[
    Procedure(   ),
    Procedure(   ),
    Procedure(   ),
    Procedure(   ),
    Procedure(   ),

]


traces :  Procedure[]


Event:
    time


Procedure -> OpenProcedure, Activity, CloseProcedure

Activity -> 
    EnterBuilding, CitizenTicket, ActivityClosed, LeaveBuilding 
    | EnterBuilding, CitizenTicket, LeaveBuilding, Activity 

CitizenTicket->
    AskDocument, ActivityOpened, CitizenGetsReceipt, 
    | ShowReceiptAction, ActivityOpened, CitizenGetsReceipt, 

AskDocument-> 
    Citizen, ShowReceiptAction
    | Citizen, 

ActivityOpened -> Activity(citizen, ticket, document=None)
CitizenGetsReceipt -> citizen.add_receipt(receipt)

EnterBuilding -> Citizen, EnterAction, Building

ActivityClosed->activity.set_closed(True)

LeaveBuilding -> Citizen, LeaveAction, Building


Rules: 
event_type_1 <  event_type_2
enter building  <  leaves building 


Sequence:
    Activity
    time 
    7:45    officer 1 enters building
    8:00    citizen 1 enters building
    8:30    officer 1 available for ticket 1, 
    9:00    citizen 1 goes to desk, 
    9:10    asks document, 
    9:20    officer 1 formally opens procedure 1
    9:30    citizen 1 receives document 1
    9:35    officer 1 available for ticket 2
    9:40    citizen 1 leaves building

    15:00   document is produced


Procedure
    citizen : Citizen
    document : Document
    procedures : Procedure[]

Activity
    officer :  Officer
    document : Document
    tasks : Task[]

Person
    name : string
    age : int
    gender: ('M','F','O')

Officer (Person)
    office : Office
    building : Building
    activity : Activity

citizen
    name : string
    (gender)

office  Anagrafe
    name : string
    building : Building      "n. 5 piazza Fiera"
    documents : Document[]   Stato famiglia, Certificato di nascita, Certificato di residenza

Building
    Address  :string    n. 5 piazza Fiera
    entities : Entity[]   

Entity   
    name : string   "Comune Trento"

"""