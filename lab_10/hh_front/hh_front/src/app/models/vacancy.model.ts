
import { InterpolationConfig } from "@angular/compiler";
import { Company } from "./company.model"; // Import the Company interface

export interface Vacancy{
    id: number; 
    name: string;
    description : string; 
    salary: number; 
    company : Company ;  // Represents a nested Company object within a Vacancy
}