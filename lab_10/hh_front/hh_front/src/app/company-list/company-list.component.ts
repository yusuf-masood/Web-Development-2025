import { Component, OnInit } from '@angular/core';
import { Company } from '../models/company.model';
import { CompanyService } from '../services/company.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-company-list',
  templateUrl: './company-list.component.html',
  styleUrls: ['./company-list.component.css']
})
export class CompanyListComponent implements OnInit {
  companies: Company[] = [];
  companySubscription: Subscription | undefined;

  constructor(private companyService: CompanyService) { }

  ngOnInit(): void {
    this.loadCompanies();
  }

  loadCompanies(): void {
    this.companySubscription = this.companyService.getCompanies()
      .subscribe(
        (companies: Company[]) => {
          this.companies = companies;
        },
        (error: any) => {
          console.error('Error loading companies:', error);
          // Optionally, handle error display or fallback logic here
        }
      );
  }

  ngOnDestroy(): void {
    // Unsubscribe to prevent memory leaks
    if (this.companySubscription) {
      this.companySubscription.unsubscribe();
    }
  }
}
