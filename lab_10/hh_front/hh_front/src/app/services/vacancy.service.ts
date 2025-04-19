// import { Injectable } from '@angular/core';
// import { HttpClient } from '@angular/common/http';
// import { Observable } from 'rxjs';
// import { Vacancy } from '../models/vacancy.model';

// @Injectable({
//   providedIn: 'root'
// })
// export class VacancyService {
//   private apiUrl = 'http://127.0.0.1:8000/api/vacancies/';

//   constructor(private http: HttpClient) { }

//   getVacanciesByCompany(companyId: number): Observable<Vacancy[]> {
//     const url = `${this.apiUrl}?company=${companyId}`;
//     return this.http.get<Vacancy[]>(url);
//   }
// }







import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Vacancy } from '../models/vacancy.model';

@Injectable({
  providedIn: 'root'
})
export class VacancyService {
  private apiUrl = 'http://127.0.0.1:8000/api'; // Update with your Django API URL

  constructor(private http: HttpClient) { }

  // Fetch vacancies for a specific company by company ID
  getVacanciesByCompany(companyId: number): Observable<Vacancy[]> {
    const url = `${this.apiUrl}/companies/${companyId}/vacancies/`;
    return this.http.get<Vacancy[]>(url);
  }
}
