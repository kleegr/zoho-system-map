# Zoho CRM Workflow Rules Export

## Summary

- **Total rules:** 31
- **Active:** 24
- **Inactive:** 7
- **Last synced:** 2026-05-20

## Rules by Module

### Phone_Calls (8 active)
- TriggerPipeDreamIVR — create_or_edit
- TriggerRettelIVR — create_or_edit
- AI - Handle Failed/Retry Phone Calls — field_update (Status)
- Failed Phone Call Notifications — field_update (Status)
- Update to Failed and Retried — field_update (Status, Call_Count, Child_Phone_Call_Id)
- Update Last Response Field — field_update (Phone_Call_Response)
- Update Agency — field_update (Update_Data)

### Service_Schedules (6 active)
- S.Schedules.Daily Clock In Call — date trigger (Next_Clock_In)
- S.Schedules.Daily Clock Out Call — date trigger (Next_Clock_Out)
- S.Schedules.Created. Generate Job Pin — on create
- S.Schedules.Created. Populate Next Call Time — on create
- S.Schedules.Updated. Generate Job Pin — field_update
- S.Schedules.Updated. Populate Next Call Time — field_update (Start_Time, End_Time)
- S.Schedules.Updated.Change Name — on edit

### Deals / Service Profiles (3 active)
- S.Profile.Populate Profile Name — create_or_edit
- S.Profiles.On Agency Updated — field_update (Agency)
- S. Profile. Update related SS based employer, provider, student — field_update

### Students (2 active)
- LSK Students: Update related records Status — field_update (Student_Status)
- Update Related Profiles and Schedules — field_update (Name)

### Providers (2 active)
- LSK Providers: Update related records Status — field_update (Provider_Status)
- Update Related Profile and Schedules — field_update (Name)

### Absentees (2 active)
- LSK Absentees: On Start Time — date trigger (Start_Time)
- LSK Absentees: On End Time — date trigger (End_Time)
