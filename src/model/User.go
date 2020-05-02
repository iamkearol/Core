package model
import time
type User struct{
	ID uint 
	Username string
	Password string
	Email email
	Dob time.Time
	Gender string
}