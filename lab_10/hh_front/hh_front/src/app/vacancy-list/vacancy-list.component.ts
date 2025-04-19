import { Component, OnInit, Input } from '@angular/core';
import { Vacancy } from '../models/vacancy.model';
import { VacancyService } from '../services/vacancy.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-vacancy-list',
  templateUrl: './vacancy-list.component.html',
  styleUrls: ['./vacancy-list.component.css']
})
export class VacancyListComponent implements OnInit {
  @Input() companyId: number = 0; // Initialize with a default value
  vacancies: Vacancy[] = [];
  vacancySubscription: Subscription | undefined;

  constructor(private vacancyService: VacancyService) { }

  ngOnInit(): void {
    this.loadVacancies();
  }

  loadVacancies(): void {
    if (this.companyId !== 0) { // Ensure companyId is valid
      this.vacancySubscription = this.vacancyService.getVacanciesByCompany(this.companyId)
        .subscribe(
          (vacancies: Vacancy[]) => {
            this.vacancies = vacancies;
          },
          (error: any) => {
            console.error('Error loading vacancies:', error);
          }
        );
    } else {
      console.error('Invalid companyId:', this.companyId);
    }
  }

  ngOnDestroy(): void {
    // Unsubscribe to prevent memory leaks
    if (this.vacancySubscription) {
      this.vacancySubscription.unsubscribe();
    }
  }
}
