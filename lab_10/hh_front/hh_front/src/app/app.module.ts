// import { NgModule } from '@angular/core';
// import { BrowserModule } from '@angular/platform-browser';

// import { AppRoutingModule } from './app-routing.module';
// import { AppComponent } from './app.component';
// import { ApiviewComponent } from './apiview/apiview.component';
// import {HttpClientModule} from '@angular/common/http';
// import { CompanyListComponent } from './company-list/company-list.component';
// import { VacancyListComponent } from './vacancy-list/vacancy-list.component' 


// @NgModule({
//   declarations: [
//     AppComponent,
//     ApiviewComponent,
//     CompanyListComponent,
//     VacancyListComponent
//   ],
//   imports: [
//     BrowserModule,
//     AppRoutingModule, 
//     HttpClientModule 
//   ],
//   providers: [],
//   bootstrap: [AppComponent]
// })
// export class AppModule { }


import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CompanyListComponent } from './company-list/company-list.component';
import { VacancyListComponent } from './vacancy-list/vacancy-list.component';

@NgModule({
  declarations: [
    AppComponent,
    CompanyListComponent,
    VacancyListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
