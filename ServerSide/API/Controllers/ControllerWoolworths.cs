using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Domain.Data.EntityFrameworkModels.Models;
using Domain.Repositories;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Components.Routing;
using Domain.Repositories.RepoInterfaces;
using Newtonsoft.Json;


namespace API.Controllers{

    [Route("api/ControllerWoolworths")]
    public class ControllerWoolworths: ControllerMain<Woolworths,RepositoryWoolworths>
    {
        public ControllerWoolworths(RepositoryWoolworths repository):base(repository)
        {
            
        }

    [HttpGet]
        public override async Task<IEnumerable<IEntity>>  Get()
        {
            return  await _repository.GetAllRecords();
        }

    }





}